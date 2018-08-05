from typing import Any, Callable, List, Optional, Tuple, Union

from django.core.checks.messages import CheckMessage, Error, Warning
from django.urls.resolvers import URLPattern, URLResolver


def check_url_config(
    app_configs: None, **kwargs: Any
) -> List[CheckMessage]: ...
def check_resolver(
    resolver: Union[URLResolver, Tuple[str, Callable], URLPattern]
) -> List[CheckMessage]: ...
def check_url_namespaces_unique(
    app_configs: None, **kwargs: Any
) -> List[Warning]: ...
def get_warning_for_invalid_pattern(pattern: Any) -> List[Error]: ...
def check_url_settings(app_configs: None, **kwargs: Any) -> List[Error]: ...
def E006(name: str) -> Error: ...