import sublime
import sublime_plugin


class InsertShebangCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "#!/usr/bin/env bash\n")
