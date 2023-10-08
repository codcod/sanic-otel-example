from importlib import import_module
from inspect import getmembers
from types import ModuleType
from typing import Union

from sanic.blueprints import Blueprint
from sanic.blueprints import BlueprintGroup


def autodiscovery(app, *module_names: Union[str, ModuleType]):
    mod = app.__module__
    blueprints = set()

    def _find_bps(module):
        nonlocal blueprints
        found_blueprints = set()
        found_blueprint_groups = set()

        for _, member in getmembers(module):
            if isinstance(member, Blueprint):
                found_blueprints.add(member)
            elif isinstance(member, BlueprintGroup):
                found_blueprint_groups.add(member)

        blueprints.update(
            found_blueprints
            - {bp for group in found_blueprint_groups for bp in group.blueprints}
        )

        blueprints.update(found_blueprint_groups)

    for module in module_names:
        if isinstance(module, str):
            module = import_module(module, mod)
        _find_bps(module)

    for bp in blueprints:
        app.blueprint(bp)
