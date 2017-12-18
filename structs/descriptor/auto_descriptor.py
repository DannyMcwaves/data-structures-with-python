from abc import ABC, abstractmethod

__all__ = ['Validator']


class AutoDescriptor:
    """
    this is the practice storage descriptor that holds references to the managing instances
    and then sets, gets or deletes them as required.
    """

    __hash = 0

    def __init__(self):
        this = self.__class__
        self.__descriptor = '__{name}#{number}'.format(name=this.__name__, number=this.__hash)
        this.__hash += 1

    def __set__(self, instance, value):
        setattr(instance, self.__descriptor, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.__descriptor) if instance else self


class Validator(ABC, AutoDescriptor):
    """
    this is a validation class the requires that some
    validations are done before values are set or gotten
    """
    @abstractmethod
    def validate(self, instance, value):
        """
        :param instance: the managing descriptor
        :param value: usually the set value
        :return: the set value if it passes the validation
        """

    def __set__(self, instance, value):
        # this part does the validation and prevents the code from reaching the setting level
        # if the validation fails or returns a None or NotImplemented value.
        value = self.validate(instance, value)
        super(Validator, self).__set__(instance, value)
