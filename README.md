# Market-Monitoring-System
Django based web application 


## app install 
- inside the *apps* folder creat app
 ```sh
 cd apps && python ../manage.py startapp *app_name* && cd ..
 ```
- app install 
```sh
 'apps.*app_name*' 
 ```
- change the name apps/*app_name*/apps.py
```sh
class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.app_name'
```

## Development
### Install `uv`
We are using [`uv`](https://astral.sh/blog/uv-unified-python-packaging) as the package manager. It needs to be installed first before running this project.

Installation in Windows:
```ps
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Installation in macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setting up the environment
Running the `uv sync` command will setup the environment with required dependencies.

### Activating the environment
Activating the environment is done with the same commands.

Windows:
```
.venv/Scripts/activate.ps1 
```
macOS/Linux:
```
source .venv/bin/activate
```

### Installing a dependency (package)
```
uv add your-package-name
```


### Use Linter and Formatter
This project uses [`ruff`](https://astral.sh/ruff) as the linter and formatter. So before submitting a PR, the contributor should use `ruff` to lint and format the code.

#### Installing `ruff`
`ruff` can be installed using by this command:
```
uv tool install ruff
uv tool update-shell
```

#### Using `ruff`
To lint the code using `ruff`:
```bash
ruff check
```
If you are satisfied with the changes it suggests, this command with apply the changes automatically:
```
ruff check --fix 
```
To format the code with `ruff`:
```
ruff format 
```
