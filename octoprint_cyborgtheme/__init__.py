# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class CyborgThemePlugin(octoprint.plugin.AssetPlugin):

    def get_assets(self):
        return dict(
            css=["css/darkly.css", "css/overrides-min.css", "css/bootstrap-modal.css"]
        )

__plugin_name__ = "Darkly Theme"
__plugin_implementation__ = CyborgThemePlugin()
