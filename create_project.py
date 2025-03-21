import os

def create_project_structure():
    project_structure = {
        'project': {
            'frontend': {
                'public': {},
                'src': {
                    'components': {},
                    'App.js': '',
                    'index.js': ''
                },
                'package.json': ''
            },
            'backend': {
                'models': {},
                'routes': {},
                'app.js': '',
                'database.js': '',
                'package.json': ''
            },
            'database': {
                'schema.sql': ''
            },
            'README.md': ''
        }
    }

    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    create_structure('.', project_structure)

create_project_structure()
