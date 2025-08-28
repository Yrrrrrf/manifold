"""Handles the dynamic, attribute-based access to asset paths."""

from __future__ import annotations

from pathlib import Path


class DynamicAssetGroup:
    """
    Represents a directory in the asset hierarchy, enabling dynamic attribute access.

    This class is the core of Manifold's intuitive API, translating attribute
    access like `assets.images.player` into file system paths.
    """

    def __init__(self, path: Path):
        self._path = path

    def __getattr__(self, name: str) -> Path | DynamicAssetGroup:
        """
        Dynamically access a file or subdirectory within this asset group.

        Args:
            name: The name of the file or directory to access.

        Returns:
            A `DynamicAssetGroup` if the name corresponds to a directory,
            or a `pathlib.Path` object if it's a file.
        """
        # First, check for a directory with the exact name
        target_path = self._path / name
        if target_path.is_dir():
            return DynamicAssetGroup(target_path)

        # If not a directory, search for a file with a matching name (extension-insensitive)
        for item in self._path.iterdir():
            if item.is_file() and item.stem == name:
                return item

        # todo: Add typo suggestions and proper error handling with AssetNotFoundError
        # Fallback for cases where the user might include the extension in the attribute
        if target_path.exists():
            return target_path
            
        raise AttributeError(f"Asset '{name}' not found in '{self._path}'")

    def __truediv__(self, other: str | Path) -> Path:
        """
        Allows joining paths using the `/` operator.

        Example:
            >>> assets.images / "player.png"

        Args:
            other: The subpath to join with the current group's path.

        Returns:
            A new `pathlib.Path` object representing the combined path.
        """
        return self._path / other

    def __repr__(self) -> str:
        return f"<DynamicAssetGroup path='{self._path}'>"
