__all__ = ['NodeValidator', 'LinkValidator']
from structs.descriptor.auto_descriptor import Validator


class NodeValidator(Validator):

    def validate(self, instance, value):
        """
        :param instance: this is the instance that's passed to the validator
        :param value: this is the original value that is supposed to be set
        :return: return the value after validation.
        """
        return value


class LinkValidator(Validator):

    type = None

    def validate(self, instance, value):
        if value is not None and value.__class__.__name__ != 'Node':
            raise ValueError('{0} is not of type {1}'.format(value, self.type))
        return value

