<!-- <img src="https://raw.githubusercontent.com/Yrrrrrf/manifold/main/resources/img/manifold.png" alt="Manifold Icon" width="128" height="128" description="A manifold that represents the concept of asset management."/> -->
<h1 align="center">

   <img src="./resources/img/manifold.png" alt="Manifold Icon" width="128" height="128" description="A manifold that represents the concept of asset management."/>
  <div align="center">manifold</div>
</h1>

<div align="center">

<!-- todo: Update badges when the package is published on PyPI -->
[![PyPI version](https://img.shields.io/pypi/v/manifold)](https://pypi.org/project/manifold/)
[![GitHub: manifold](https://img.shields.io/badge/GitHub-manifold-181717?logo=github)](https://github.com/Yrrrrrf/manifold)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/)
<!-- [![Downloads](https://pepy.tech/badge/manifold)](https://pepy.tech/project/manifold) -->

</div>

## Overview

A Python library for zero-configuration, OS-independent asset management. It automatically discovers and provides an intuitive API to access project files, eliminating the need for hardcoded relative paths or complex configuration.

Built on top of Python's native `pathlib`, manifold  eliminates boilerplate code related to path management. It adapts to your existing project structure, allowing you to focus on your application's logic instead of worrying about file locations.

## Key Features

- **Zero Configuration**: Works out-of-the-box by automatically detecting your project root and common asset directories.
- **Intuitive, Pythonic API**: Access your assets as if they were Python objects (`assets.images.player_icon`).
- **Cross-Platform Reliability**: Identical behavior across Windows, macOS, and Linux.
- **`pathlib` Integration**: Returns standard `pathlib.Path` objects for full compatibility with modern Python libraries.
- **Path-like Behavior**: Supports natural path joining with the `/` operator (`assets.fonts / "main.ttf"`).
- **Excellent Developer Experience**: Provides clear, helpful error messages with suggestions for typos.

## Installation

```bash
pip install pathlight
```

## Quick Start

Imagine you have the following project structure:

```
my_awesome_project/
├── assets/
│   ├── images/
│   │   ├── player.png
│   │   └── background.jpg
│   └── fonts/
│       └── main.ttf
└── src/
    └── main.py
```

Now, from your `main.py` file, you can access your assets effortlessly:

```python
# src/main.py
from pathlight import assets
from pathlib import Path

# Access a file directly via attribute access
# Note: File extensions are automatically handled and can be omitted.
player_image_path = assets.assets.images.player

# The returned object is a standard pathlib.Path object
print(f"Player image is a Path object: {isinstance(player_image_path, Path)}")
print(f"Path to player image: {player_image_path}")

# You can also use the / operator for path joining
font_path = assets.assets.fonts / "main.ttf"
print(f"Path to font: {font_path}")

# Check for existence
if "background.jpg" in assets.assets.images:
    print("Background image found!")
```

## API Behavior

pathlight dynamically maps your directory structure to a Python object.

-   **Directory Access**: `assets.images` maps to the first discoverable directory named `images/`.
-   **File Access**: `assets.images.player_png` maps to the file `images/player.png`. The file extension is optional and normalized.
-   **Path Joining**: `assets.images / "enemies/goblin.png"` works just like `pathlib`.
-   **Iteration**: `for file in assets.images: print(file)` allows you to iterate over contents.

## Usage Examples

See the [examples](./examples) directory for complete sample applications demonstrating various project layouts and use cases.

<!-- todo: Add a basic example to the examples directory -->

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.