# Shareable Admonition Plugin for MkDocs

The Shareable Admonition Plugin is a custom extension for MkDocs, a static site generator geared towards project documentation. This plugin enhances the documentation by allowing the inclusion of shareable admonitions with embedded images and descriptions directly within your Markdown files.

## Features
* Admonition with Images: Easily embed images within admonitions to make your documentation more engaging and informative.
* Customizable Admonitions: Supports MkDocs' native admonition syntax with the added capability to include images and custom text.
* Automatic Image and Text Extraction: Automatically extracts the first image and text from the admonition block for display.

## Installation

To install the Shareable Admonition Plugin, you can use pip:

```bash
pip install shareable-admonition-plugin
```

## Configuration
After installation, you need to activate the plugin in your mkdocs.yml configuration file:

### Update mkdocs.yaml

```yaml
plugins:
  - search
  - shareable_admonition

extra_javascript:
  - javascripts/copy-link.js

google_tag: !ENV GOOGLE_ANALYTICS_KEY
```

Ensure that you also include any other plugins you wish to use.

### Copy the css and javascript 

Copy the `docs/stylesheets/share-card.css` into `stylesheets` folder in your docs directory.
Copy the `docs/javascripts/copy-link.js` into `javascripts` folder in your docs directory. 

## Usage
To use the plugin, simply include an admonition in your Markdown file as you normally would, but now you can also embed an image and a description, with the url `note-slug`:

```markdown
!!! note "This is a custom note" note-slug
    ![Image Alt Text](image_url.jpg)
    This is a description that will be extracted along with the image.
```

The plugin supports the standard MkDocs admonition types (note, warning, tip, etc.) and allows for the inclusion of images either by using Markdown image syntax or HTML <img> tags.

## Development
This plugin is developed using Python and integrates with MkDocs through its plugin system. It uses regular expressions to parse admonitions and extract relevant information, and Jinja2 for templating.

## Contributing
Contributions to the Shareable Admonition Plugin are welcome. Please feel free to submit pull requests or create issues for bugs and feature requests on the project's GitHub page.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
