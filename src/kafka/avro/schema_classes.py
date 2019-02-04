import json
import os.path
import decimal
import datetime
import six
from avrogen.dict_wrapper import DictWrapper
from avrogen import avrojson
from avro import schema as avro_schema
if six.PY3:    from avro.schema import SchemaFromJSONData as make_avsc_object

else:
    from avro.schema import make_avsc_object



def __read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()

def __get_names_and_schema(file_name):
    names = avro_schema.Names()
    schema = make_avsc_object(json.loads(__read_file(file_name)), names)
    return names, schema

__NAMES, SCHEMA = __get_names_and_schema(os.path.join(os.path.dirname(__file__), "schema.avsc"))
__SCHEMAS = {}
def get_schema_type(fullname):
    return __SCHEMAS.get(fullname)
__SCHEMAS = dict((n.fullname.lstrip("."), n) for n in six.itervalues(__NAMES.names))


class SchemaClasses(object):


    pass
    class it(object):
        class genero(object):

            class PRO_clip_repositoryClass(DictWrapper):

                """

                """


                RECORD_SCHEMA = get_schema_type("it.genero.PRO_clip_repository")


                def __init__(self, inner_dict=None):
                    super(SchemaClasses.it.genero.PRO_clip_repositoryClass, self).__init__(inner_dict)
                    if inner_dict is None:
                        self.idclip = int()
                        self.url_src = None
                        self.url = None
                        self.file = None
                        self.title = None
                        self.description = None
                        self.text = None
                        self.language = None
                        self.todo = SchemaClasses.it.genero.PRO_clip_repositoryClass.RECORD_SCHEMA.fields[9].default
                        self.pubDate = None
                        self.IP = None
                        self.subject = None
                        self.prop_select = None
                        self.prop_neglect = None


                @property
                def idclip(self):
                    """
                    :rtype: int
                    """
                    return self._inner_dict.get('idclip')

                @idclip.setter
                def idclip(self, value):
                    #"""
                    #:param int value:
                    #"""
                    self._inner_dict['idclip'] = value


                @property
                def url_src(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('url_src')

                @url_src.setter
                def url_src(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['url_src'] = value


                @property
                def url(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('url')

                @url.setter
                def url(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['url'] = value


                @property
                def file(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('file')

                @file.setter
                def file(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['file'] = value


                @property
                def title(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('title')

                @title.setter
                def title(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['title'] = value


                @property
                def description(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('description')

                @description.setter
                def description(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['description'] = value


                @property
                def text(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('text')

                @text.setter
                def text(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['text'] = value


                @property
                def language(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('language')

                @language.setter
                def language(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['language'] = value


                @property
                def insertdate(self):
                    """
                    :rtype: int
                    """
                    return self._inner_dict.get('insertdate')

                @insertdate.setter
                def insertdate(self, value):
                    #"""
                    #:param int value:
                    #"""
                    self._inner_dict['insertdate'] = value


                @property
                def todo(self):
                    """
                    :rtype: int
                    """
                    return self._inner_dict.get('todo')

                @todo.setter
                def todo(self, value):
                    #"""
                    #:param int value:
                    #"""
                    self._inner_dict['todo'] = value


                @property
                def pubDate(self):
                    """
                    :rtype: int
                    """
                    return self._inner_dict.get('pubDate')

                @pubDate.setter
                def pubDate(self, value):
                    #"""
                    #:param int value:
                    #"""
                    self._inner_dict['pubDate'] = value


                @property
                def IP(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('IP')

                @IP.setter
                def IP(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['IP'] = value


                @property
                def subject(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('subject')

                @subject.setter
                def subject(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['subject'] = value


                @property
                def prop_select(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('prop_select')

                @prop_select.setter
                def prop_select(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['prop_select'] = value


                @property
                def prop_neglect(self):
                    """
                    :rtype: str
                    """
                    return self._inner_dict.get('prop_neglect')

                @prop_neglect.setter
                def prop_neglect(self, value):
                    #"""
                    #:param str value:
                    #"""
                    self._inner_dict['prop_neglect'] = value


            pass

__SCHEMA_TYPES = {
'it.genero.PRO_clip_repository': SchemaClasses.it.genero.PRO_clip_repositoryClass,

}
_json_converter = avrojson.AvroJsonConverter(use_logical_types=False, schema_types=__SCHEMA_TYPES)
