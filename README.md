# GenericSite: Rapid website prototyping with Django

Django is famous for being a batteries-included web framework for perfectionists with
deadlines. However, bootstrapping a new website using Django still requires you to write
a significant amount of Python code and HTML templates to generate the basics needed by
most every website.

GenericSite is a Django app designed to get you that first 80% of your website
functionality as quickly as possible. It performs the undifferentiated heavy lifting so
you can focus on the 20% of the work that makes your site special.

GenericSite defines a data model based on [Schema.org](https://schema.org), extended in
some places using fields from the [open graph protocol](https://ogp.me), or other web
standards. It provides concrete Django models for common web objects, as well as an
abstract CreativeWork model for extending the available page types.

GenericSite includes a set of views to be used with the included models. These are based
on Django's generic class-based views. They can be used directly or subclassed to meet
your needs.

GenericSite includes a set of templates using the
[Bootstrap CSS framework](https://getbootstrap.com) based on the examples found on the
bootstrap website. The templates work with any objects that implement the generic data
model, or anything that you can map to an opengraph-like model. They can easily be
coupled with Django's generic class-based views to produce a clean and professional site
quickly and easily. If you use the included concrete models with the default templates
and the included views, you'll be starting with a basic blog-style site.

The templates are built using Bootstrap 5, and they load the core CSS and JavaScript
from a CDN by default, so there's nothing else to install and little or no front-end to
deal with.

## Development

After checking out the code, you can bootstrap a development environment by running:

```sh
python manage.py devsetup
```

Note that the Python used to run this script will be the one used in your virtualenv.

## How to use it

Add the following to your `settings.py`:

```python
import genericsite.apps
INSTALLED_APPS = [
  *genericsite.apps.CONTENT
  # Optionally use tinymce in the admin
  "tinymce",
  # Other Django apps here, then
  *genericsite.apps.ADMIN
]
MIDDLEWARE += [
  "django.contrib.sites.middleware.CurrentSiteMiddleware",
  "genericsite.redirects.TemporaryRedirectFallbackMiddleware",
]
# If using tinymce
TINYMCE_DEFAULT_CONFIG = genericsite.apps.TINYMCE_CONFIG

# Add `genericsite.apps.context_defaults` to your context processors. You will also
# need to add the request, auth, and messages context processors if not already there.
# Probably looks like this:
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "genericsite.apps.context_defaults",
            ],
        },
    },
]

```

In your project's `urls.py`, insert the GenericSite URLs where you want them. To have
GenericSite manage your home page and top-level pages, make it the LAST url pattern, and
list it like this:

```python
from genericsite import views as generic

urlpatterns = [
    # GenericSite provides templates for auth pages
    path("accounts/", include("django.contrib.auth.urls")),
    # You need to add the admin yourself:
    path("admin/", admin.site.urls),
    # TinyMCE urls if desired
    path("tinymce/", include("tinymce.urls")),
    # All other urls are handed to GenericSite
    path("", include("genericsite.urls")),
]
```

TODO: When closer to "1.0" create a project template for use with startproject.

### The base template

The GenericSite base template is divided into major blocks that can be replaced in your
child templates. The blocks, in order of appearance, are:

- `title`: The content of the HTML page title tag.
- `bootstrap_styles`: An HTML block that by default pulls in the bootstrap stylesheet.
  You can override it to customize your version of bootstrap (e.g. with BootSwatch) or
  include `{{ block.super }}` and then add some tweaks.
- `opengraph`: Used to expose the page's open graph metadata in the HTML head. This is
  done in the default template. You won't need to override this unless you define custom
  open graph types that need special handling.
- `extra_head`: Override this if you need to include custom CSS, web fonts, etc. in the
  page's HTML head.
- `body_class`: A block you can override to apply a custom class to the HTML body
  element, if needed by your custom CSS.
- `header`: A block to contain your site's masthead and main navigation, the header
  elements common to every page. Override in your site's base template.
- `precontent`: A block that appears before the main content of the page. Override this
  on home pages or section pages where you need to insert some feature above the
  standard content, such as a call to action, introduction to the topic, featured
  stories, etc.
- `content`: The main content body of the page. By default, will `include` the content
  sub-template specified in the template context. For an Article this will be the
  article text, for a Section page this will be the list of Articles in the Section.
- `postcontent`: A block that appears after the main content of the page. Often used to
  include "Read Next" or "Related" recirculation modules or a call to action.
- `footer`: A block to contain your site's footer links and blanket copyright
  statements, elements common to every page. Override in your site's base template.
- `bootstrap_js`: An HTML that by default loads the Bootstrap JS bundle. Override if
  needed.
- `extra_js`: A block just before the closing body tag. Use this to include deferred
  JavaScript or other elements you want loaded after the main page content.

### Block Templates

Genericsite ships with several partial templates that can be included as the content of
the base blocks to construct a page quickly from reusable modules.

TODO: Document available block templates.

### Site Vars

The app comes with a SiteVar model for storing site-specific variables or chunks of
content. You can store any variable for use with your own templates. Variables used by
the default templates/models can be found on the Admin Documentation page for SiteVar.

## Images and Media

GenericSite takes advantage of Django Imagekit to manage images. Models are provided for
storing file metadata including copyright information.

GenericSite uses presets to produce images in specific sizes as recommended by
[Buffer's Social Media Image Guidelines](https://buffer.com/library/ideal-image-sizes-social-media-posts/).

These named thumbnail settings are available:

- small: 160x90
- medium: 400x225
- large: 960x540
- opengraph: 1200x630
- hd720p: 1280x720
- hd1080p: 1920x1080
- portrait_small: 90x160
- portrait_medium: 225x400
- portrait_large: 540x960
- portrait_cover: 1000x1500
- portrait_social: 1080x1350
- portrait_hd: 1080x1920
