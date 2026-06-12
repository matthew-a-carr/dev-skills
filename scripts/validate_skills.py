#!/usr/bin/env python3
"""Skill spec compliance gate. Mirrors .github/workflows/validate.yml:
exit 0 = clean, 1 = errors (fail), 2 = warnings-only (allow), 3 = CLI bug."""
import subprocess
import sys

rc = subprocess.run(["go", "tool", "skill-validator", "check", "skills/"]).returncode
sys.exit(0 if rc == 2 else rc)
