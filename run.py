import wrapt
#https://www.cnpython.com/pypi/wrapt

def logging(level='INFO'):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        print("[{}]: enter {}()".format(level, wrapped.__name__))
        return wrapped(*args, **kwargs)
    return wrapper

@logging()
def do(work):
    print('do {}'.format(work)) 

@logging(level='WARN')
def doo(work):
    print('do {}'.format(work)) 

if __name__ == "__main__":
    do('it!')
    doo('it!')
