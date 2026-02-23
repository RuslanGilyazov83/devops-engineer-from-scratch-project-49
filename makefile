VERSION = 0.1.0
PACKAGE_NAME = hexlet_code

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/$(PACKAGE_NAME)-$(VERSION)-py3-none-any.whl

lint:
	uv run ruff check brain_games