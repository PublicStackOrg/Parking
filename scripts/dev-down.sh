#!/usr/bin/env bash
# Parking — stop the local dev stack.
set -euo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
docker compose down
