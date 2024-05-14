import logging

def deprecated(message):
  def deprecated_decorator(callable):
      def deprecated_callable(*args, **kwargs):
          logging.warn("{} is a deprecated callable. {}".format(callable.__name__, message))
          return callable(*args, **kwargs)
      return deprecated_callable
  return deprecated_decorator
