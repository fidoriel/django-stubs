from datetime import date, datetime, time, timedelta
from decimal import Context, Decimal
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from uuid import UUID

from django.core.validators import DecimalValidator
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model
from django.db.models.expressions import Col, CombinedExpression
from django.db.models.fields import reverse_related
from django.db.models.fields.files import FieldFile
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.query import QuerySet
from django.db.models.query_utils import RegisterLookupMixin
from django.db.models.sql.compiler import SQLCompiler, SQLInsertCompiler
from django.forms.fields import BooleanField, DurationField, EmailField, Field, FloatField, TypedMultipleChoiceField
from django.utils.datastructures import DictWrapper

class Empty: ...
class NOT_PROVIDED: ...

BLANK_CHOICE_DASH: Any

class Field(RegisterLookupMixin):
    empty_strings_allowed: bool = ...
    empty_values: Any = ...
    creation_counter: int = ...
    auto_creation_counter: int = ...
    default_validators: Any = ...
    default_error_messages: Any = ...
    system_check_deprecated_details: Any = ...
    system_check_removed_details: Any = ...
    hidden: bool = ...
    many_to_many: Any = ...
    many_to_one: Any = ...
    one_to_many: Any = ...
    one_to_one: Any = ...
    related_model: Any = ...
    description: Any = ...
    name: Any = ...
    verbose_name: Any = ...
    primary_key: Any = ...
    remote_field: Any = ...
    is_relation: Any = ...
    default: Any = ...
    editable: Any = ...
    serialize: Any = ...
    unique_for_date: Any = ...
    unique_for_month: Any = ...
    unique_for_year: Any = ...
    choices: Any = ...
    help_text: Any = ...
    db_index: Any = ...
    db_column: Any = ...
    auto_created: Any = ...
    error_messages: Any = ...
    def __init__(
        self,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        primary_key: bool = ...,
        max_length: Optional[int] = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: bool = ...,
        db_index: bool = ...,
        rel: Optional[ForeignObjectRel] = ...,
        default: Any = ...,
        editable: bool = ...,
        serialize: bool = ...,
        unique_for_date: None = ...,
        unique_for_month: None = ...,
        unique_for_year: None = ...,
        choices: Optional[
            Union[
                List[List[Union[List[List[str]], str]]],
                List[Tuple[Optional[int], str]],
                List[Tuple[Union[int, str], int]],
                Tuple[Tuple[Union[int, str], Union[int, str]]],
            ]
        ] = ...,
        help_text: str = ...,
        db_column: Optional[str] = ...,
        db_tablespace: Optional[str] = ...,
        auto_created: bool = ...,
        validators: Union[List[Callable], Tuple] = ...,
        error_messages: None = ...,
    ) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def get_col(self, alias: str, output_field: Optional[Union[Field, reverse_related.ForeignObjectRel]] = ...) -> Col: ...
    def cached_col(self) -> Col: ...
    def select_format(
        self, compiler: SQLCompiler, sql: str, params: List[Union[int, str]]
    ) -> Tuple[str, List[Union[int, str]]]: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, List[Tuple[int, str]]]]: ...
    def clone(self) -> Field: ...
    def __eq__(self, other: Field) -> bool: ...
    def __lt__(self, other: Field) -> bool: ...
    def __hash__(self) -> int: ...
    def __deepcopy__(self, memodict: Dict[int, Dict[Any, Any]]) -> Field: ...
    def __copy__(self) -> Field: ...
    def __reduce__(self): ...
    def get_pk_value_on_save(self, instance: Model) -> Optional[UUID]: ...
    def to_python(self, value: FieldFile) -> FieldFile: ...
    def validators(self) -> List[Callable]: ...
    def run_validators(self, value: Any) -> None: ...
    def validate(self, value: Any, model_instance: Optional[Model]) -> None: ...
    def clean(self, value: Any, model_instance: Optional[Model]) -> Any: ...
    def db_type_parameters(self, connection: DatabaseWrapper) -> DictWrapper: ...
    def db_check(self, connection: DatabaseWrapper) -> None: ...
    def db_type(self, connection: DatabaseWrapper) -> str: ...
    def rel_db_type(self, connection: DatabaseWrapper) -> str: ...
    def cast_db_type(self, connection: Any): ...
    def db_parameters(self, connection: DatabaseWrapper) -> Dict[str, Optional[str]]: ...
    def db_type_suffix(self, connection: DatabaseWrapper) -> Optional[str]: ...
    def get_db_converters(self, connection: DatabaseWrapper) -> List[Callable]: ...
    @property
    def unique(self) -> bool: ...
    @property
    def db_tablespace(self) -> str: ...
    concrete: Any = ...
    def set_attributes_from_name(self, name: str) -> None: ...
    model: Any = ...
    def contribute_to_class(self, cls: Type[Model], name: str, private_only: bool = ...) -> None: ...
    def get_filter_kwargs_for_object(self, obj: Any): ...
    def get_attname(self) -> str: ...
    def get_attname_column(self) -> Tuple[str, str]: ...
    def get_internal_type(self) -> str: ...
    def pre_save(self, model_instance: Model, add: bool) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...
    def get_db_prep_value(
        self, value: Any, connection: DatabaseWrapper, prepared: bool = ...
    ) -> Optional[Union[bytes, float, str]]: ...
    def get_db_prep_save(self, value: Any, connection: DatabaseWrapper) -> Optional[Union[float, str]]: ...
    def has_default(self) -> bool: ...
    def get_default(self) -> Any: ...
    def get_choices(
        self,
        include_blank: bool = ...,
        blank_choice: List[Tuple[str, str]] = ...,
        limit_choices_to: Optional[Dict[str, QuerySet]] = ...,
    ) -> List[Tuple[Union[int, str], Union[Tuple[Tuple[str, str], Tuple[str, str]], str]]]: ...
    def value_to_string(self, obj: Model) -> str: ...
    flatchoices: Any = ...
    def save_form_data(self, instance: Model, data: Optional[Union[date, Model, float, str]]) -> None: ...
    def formfield(
        self,
        form_class: Optional[Type[Field]] = ...,
        choices_form_class: Optional[Type[TypedMultipleChoiceField]] = ...,
        **kwargs: Any
    ) -> Field: ...
    def value_from_object(self, obj: Model) -> Any: ...

class AutoField(Field):
    description: Any = ...
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, Union[bool, str]]]: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Union[int, str]) -> int: ...
    def rel_db_type(self, connection: DatabaseWrapper) -> str: ...
    def validate(self, value: Any, model_instance: Any) -> None: ...
    def get_db_prep_value(self, value: Union[int, str], connection: DatabaseWrapper, prepared: bool = ...) -> Union[int, str]: ...
    def get_prep_value(self, value: Optional[Union[int, str]]) -> Optional[int]: ...
    def contribute_to_class(self, cls: Type[Model], name: str, **kwargs: Any) -> None: ...
    def formfield(self, **kwargs: Any) -> None: ...
    def __get__(self, instance, owner) -> int: ...

class BigAutoField(AutoField):
    description: Any = ...
    def get_internal_type(self) -> str: ...
    def rel_db_type(self, connection: DatabaseWrapper) -> str: ...

class BooleanField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[bool, str]]) -> bool: ...
    def get_prep_value(self, value: Optional[Union[bool, str]]) -> Optional[bool]: ...
    def formfield(self, **kwargs: Any) -> BooleanField: ...

class CharField(Field):
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def cast_db_type(self, connection: Any): ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[Model, int, str]]) -> Optional[str]: ...
    def get_prep_value(self, value: Optional[Union[Model, str]]) -> Optional[str]: ...
    def formfield(self, **kwargs: Any) -> Field: ...
    def __get__(self, instance, owner) -> str: ...

class CommaSeparatedIntegerField(CharField):
    default_validators: Any = ...
    description: Any = ...
    system_check_removed_details: Any = ...

class DateTimeCheckMixin:
    def check(self, **kwargs: Any) -> List[Any]: ...

class DateField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(
        self, verbose_name: Optional[str] = ..., name: None = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs: Any
    ) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, Union[Callable, int, str]]]: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[date, str]]) -> Optional[date]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Optional[Union[date, CombinedExpression]]: ...
    def contribute_to_class(self, cls: Type[Model], name: str, **kwargs: Any) -> None: ...
    def get_prep_value(self, value: Optional[Union[date, str]]) -> Optional[date]: ...
    def get_db_prep_value(self, value: Optional[date], connection: DatabaseWrapper, prepared: bool = ...) -> Optional[str]: ...
    def value_to_string(self, obj: Model) -> str: ...
    def formfield(self, **kwargs: Any) -> Field: ...

class DateTimeField(DateField):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[datetime, str]]) -> Optional[datetime]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Optional[Union[datetime, CombinedExpression]]: ...
    def get_prep_value(self, value: Optional[datetime]) -> Optional[datetime]: ...
    def get_db_prep_value(
        self, value: Optional[datetime], connection: DatabaseWrapper, prepared: bool = ...
    ) -> Optional[str]: ...
    def value_to_string(self, obj: Model) -> str: ...
    def formfield(self, **kwargs: Any) -> Field: ...

class DecimalField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(
        self,
        verbose_name: None = ...,
        name: None = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        **kwargs: Any
    ) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def validators(self) -> List[DecimalValidator]: ...
    def context(self) -> Context: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, int]]: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[str]) -> Optional[Decimal]: ...
    def get_db_prep_save(self, value: Optional[str], connection: DatabaseWrapper) -> Optional[str]: ...
    def get_prep_value(self, value: None) -> None: ...
    def formfield(self, **kwargs: Any): ...

class DurationField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: str) -> timedelta: ...
    def get_db_prep_value(self, value: Any, connection: Any, prepared: bool = ...): ...
    def get_db_converters(self, connection: Any): ...
    def value_to_string(self, obj: Model) -> str: ...
    def formfield(self, **kwargs: Any) -> DurationField: ...

class EmailField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, int]]: ...
    def formfield(self, **kwargs: Any) -> EmailField: ...

class FilePathField(Field):
    description: Any = ...
    def __init__(
        self,
        verbose_name: Optional[Any] = ...,
        name: Optional[Any] = ...,
        path: str = ...,
        match: Optional[Any] = ...,
        recursive: bool = ...,
        allow_files: bool = ...,
        allow_folders: bool = ...,
        **kwargs: Any
    ) -> None: ...
    def check(self, **kwargs: Any): ...
    def deconstruct(self): ...
    def get_prep_value(self, value: Optional[str]) -> Optional[str]: ...
    def get_internal_type(self): ...

class FloatField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def get_prep_value(self, value: Union[float, str]) -> float: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Union[float, str]) -> float: ...
    def formfield(self, **kwargs: Any) -> FloatField: ...

class IntegerField(Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def validators(self) -> List[Any]: ...
    def get_prep_value(self, value: Optional[Union[int, str]]) -> Optional[int]: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Union[int, str]) -> int: ...

class BigIntegerField(IntegerField):
    empty_strings_allowed: bool = ...
    description: Any = ...
    MAX_BIGINT: int = ...
    def get_internal_type(self) -> str: ...

class IPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    system_check_removed_details: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self) -> Tuple[None, str, List[Any], Dict[str, bool]]: ...
    def get_prep_value(self, value: Any): ...
    def get_internal_type(self) -> str: ...

class GenericIPAddressField(Field):
    empty_strings_allowed: bool = ...
    description: Any = ...
    default_error_messages: Any = ...
    unpack_ipv4: Any = ...
    protocol: Any = ...
    def __init__(
        self,
        verbose_name: Optional[Any] = ...,
        name: Optional[Any] = ...,
        protocol: str = ...,
        unpack_ipv4: bool = ...,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
    def check(self, **kwargs: Any): ...
    def deconstruct(self): ...
    def get_internal_type(self): ...
    def to_python(self, value: Union[Callable, int, str]) -> str: ...
    def get_db_prep_value(self, value: Optional[str], connection: DatabaseWrapper, prepared: bool = ...) -> Optional[str]: ...
    def get_prep_value(self, value: Optional[str]) -> Optional[str]: ...

class NullBooleanField(BooleanField):
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self): ...
    def get_internal_type(self): ...

class PositiveIntegerRelDbTypeMixin:
    def rel_db_type(self, connection: Any): ...

class PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self) -> str: ...

class PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description: Any = ...
    def get_internal_type(self) -> str: ...

class SlugField(CharField):
    default_validators: Any = ...
    description: Any = ...
    allow_unicode: Any = ...
    def __init__(
        self, *args: Any, max_length: int = ..., db_index: bool = ..., allow_unicode: bool = ..., **kwargs: Any
    ) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, int]]: ...
    def get_internal_type(self) -> str: ...

class SmallIntegerField(IntegerField):
    description: Any = ...
    def get_internal_type(self) -> str: ...

class TextField(Field):
    description: Any = ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[Dict[Any, Any], int, str]]) -> Optional[str]: ...
    def get_prep_value(self, value: Optional[Union[Dict[Any, Any], int, str]]) -> Optional[str]: ...

class TimeField(DateTimeCheckMixin, Field):
    empty_strings_allowed: bool = ...
    default_error_messages: Any = ...
    description: Any = ...
    def __init__(
        self, verbose_name: None = ..., name: None = ..., auto_now: bool = ..., auto_now_add: bool = ..., **kwargs: Any
    ) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[Any, Any]]: ...
    def get_internal_type(self) -> str: ...
    def to_python(self, value: Optional[Union[datetime, str]]) -> Optional[time]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Optional[datetime]: ...
    def get_prep_value(self, value: Optional[datetime]) -> Optional[time]: ...
    def get_db_prep_value(
        self, value: Optional[datetime], connection: DatabaseWrapper, prepared: bool = ...
    ) -> Optional[str]: ...
    def value_to_string(self, obj: Any): ...

class URLField(CharField):
    default_validators: Any = ...
    description: Any = ...
    def __init__(self, verbose_name: None = ..., name: None = ..., **kwargs: Any) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, int]]: ...

class BinaryField(Field):
    description: Any = ...
    empty_values: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, bool]]: ...
    def get_internal_type(self) -> str: ...
    def get_placeholder(self, value: None, compiler: SQLInsertCompiler, connection: DatabaseWrapper) -> str: ...
    def get_default(self) -> bytes: ...
    def get_db_prep_value(self, value: Optional[bytes], connection: DatabaseWrapper, prepared: bool = ...) -> None: ...
    def value_to_string(self, obj: Any): ...
    def to_python(self, value: Any): ...

class UUIDField(Field):
    default_error_messages: Any = ...
    description: str = ...
    empty_strings_allowed: bool = ...
    def __init__(self, verbose_name: None = ..., **kwargs: Any) -> None: ...
    def deconstruct(self) -> Tuple[Optional[str], str, List[Any], Dict[str, Union[Callable, bool]]]: ...
    def get_internal_type(self) -> str: ...
    def get_db_prep_value(
        self, value: Optional[Union[Dict[Any, Any], List[Any]]], connection: DatabaseWrapper, prepared: bool = ...
    ) -> None: ...
    def to_python(self, value: Optional[Union[Dict[Any, Any], List[Any], UUID]]) -> Optional[UUID]: ...