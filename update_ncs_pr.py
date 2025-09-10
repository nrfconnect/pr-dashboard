#!/usr/bin/env python3

# Copyright 2024 Google LLC
# Copyright (c) 2024 The Linux Foundation
# SPDX-License-Identifier: Apache-2.0

from west.manifest import Manifest, ImportFlag
from west.manifest import ManifestProject
import re
import subprocess

manifest = Manifest.from_file(import_flags=ImportFlag.IGNORE_PROJECTS)

repos = ["sdk-nrf"]
for project in manifest.get_projects([]):
    if not manifest.is_active(project):
        continue

    if isinstance(project, ManifestProject):
        continue

    m = re.match(r"https://github\.com/([\w\-]+)/([\w\-]+)", project.url)

    if m and len(m.groups()) == 2 and m[1] == 'nrfconnect':
        repos.append(m[2])

repos_arg = ",".join(repos)

print(repos)

subprocess.run(["python", "-u", "update_pr.py", "-o", "nrfconnect",
                "--repos", repos_arg])
