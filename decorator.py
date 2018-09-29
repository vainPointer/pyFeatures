import logging
# 装饰器：在不改变原函数功能的前提下增加新的功能。
# 将原函数主功能与插入日志、性能测试、事务处理、缓存、权限校验等需要大量重复代码实现的功能分离。


def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def logging_with_params(param_level):
    def decorator(func):
        def warpper(*args, **kwargs):
            if param_level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif param_level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return warpper
    return decorator


# @use_logging
@logging_with_params("warn")
def working_func(job, time=0):
    print("I'm doing %s, time is %i" % (job, time))


if __name__ == '__main__':
    working_func("programming")
