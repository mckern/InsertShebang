import sublime
import sublime_plugin

class InsertShebangCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        window.show_input_panel("Interpreter:", "bash",
                                self.on_done, None, None)

    def on_done(self, input_string):
        self.view.run_command("move_to", {"to": "bof"})
        self.view.run_command("insert", {"characters": "#!/usr/bin/env " + input_string + "\n"})
