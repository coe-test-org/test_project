"""Check that basic features work.

Catch cases where e.g. files are missing so the import doesn't work. It is
recommended to check that e.g. assets are included."""

from test_project.helpers import func

message = func()
if message == "hi":
    print("Smoke test succeeded")
else:
    raise RuntimeError(message)
