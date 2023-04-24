from simple_example import *
from jinja2 import Environment, select_autoescape

# Setup jinja environment
env = Environment(autoescape=select_autoescape())

def generate_webpage():
    """Generates a page listing taxonomies
    
    Notes
    -----
    - You need to install Jinja (https://jinja.palletsprojects.com/en/3.1.x/) to use this
    """
    template = env.from_string(r'''
<!doctype html>
<html lang="en">

<head>
  <title>Homepage</title>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS v5.2.1 -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

</head>

<body>

    <div class="row">
        <div class="col-md-12 text-center">
            <h1>Taxonomies</h1>
        </div>

        <div class="col-md-2 spacer">
        </div>
        <div class="col-md-8">
            {% for category in categories %}
                <hr>
                <div class="row">
                    <div class="col-md-12 text-center">
                        <h2>{{category.name}}</h2>
                    </div>
                </div>
                {% if category.children %}
                    {% for child in category.children %}
                        <div class="row">
                            <div class="col-md-12 text-center">
                                <h4>{{child.name}}</h4>
                            </div>
                        </div>
                    {% endfor %}
                {% endif %}
                <div class="row">
                    <div class="col-md-12 text-center">
                        <h2>Products</h2>
                    </div>
                    {% for product in category.get_products() %}
                    <div class="col-md-12 text-center">
                        <h4>{{product.name}}</h4>
                    </div>
                    {%endfor%}
                </div>
            {% endfor %}
        </div>
        <div class="col-md-2 spacer">
        </div>
    </div>

  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous">
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous">
  </script>
</body>

</html>
    ''')

    return template.render(categories=[computers,phones,brands])

def export_webpage(filename="index.html"):
    content = generate_webpage()
    with open(filename, "w+") as output_file:
        output_file.write(content)
        
if __name__ == "__main__":
    export_webpage()
