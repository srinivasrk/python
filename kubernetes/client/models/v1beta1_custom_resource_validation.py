# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CustomResourceValidation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'open_apiv3_schema': 'V1beta1JSONSchemaProps'
    }

    attribute_map = {
        'open_apiv3_schema': 'openAPIV3Schema'
    }

    def __init__(self, open_apiv3_schema=None):
        """
        V1beta1CustomResourceValidation - a model defined in Swagger
        """

        self._open_apiv3_schema = None
        self.discriminator = None

        if open_apiv3_schema is not None:
          self.open_apiv3_schema = open_apiv3_schema

    @property
    def open_apiv3_schema(self):
        """
        Gets the open_apiv3_schema of this V1beta1CustomResourceValidation.
        OpenAPIV3Schema is the OpenAPI v3 schema to be validated against.

        :return: The open_apiv3_schema of this V1beta1CustomResourceValidation.
        :rtype: V1beta1JSONSchemaProps
        """
        return self._open_apiv3_schema

    @open_apiv3_schema.setter
    def open_apiv3_schema(self, open_apiv3_schema):
        """
        Sets the open_apiv3_schema of this V1beta1CustomResourceValidation.
        OpenAPIV3Schema is the OpenAPI v3 schema to be validated against.

        :param open_apiv3_schema: The open_apiv3_schema of this V1beta1CustomResourceValidation.
        :type: V1beta1JSONSchemaProps
        """

        self._open_apiv3_schema = open_apiv3_schema

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CustomResourceValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
