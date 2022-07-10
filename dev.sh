COMPOSE_FILE=$(readlink -f local.yml)
export COMPOSE_FILE

# Wrapper command
dockerpy(){
  docker-compose run --rm --no-deps -w /app --entrypoint "bash -c 'source .venv/bin/activate && $*'" django
}

managepy(){
  dockerpy python manage.py "$@"
}

helpmanage(){
  dockerpy python manage.py "$1" --help
}

# Docker related
alias runserver='docker-compose up -d'
alias logs='docker-compose logs --no-log-prefix -f django'

# Python related
alias pyterm="dockerpy bash"
alias djshell="managepy shell"
