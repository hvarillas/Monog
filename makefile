flake8:
	python -m flake8 --exclude=venv,__pycache__ --max-line-length=100
mypy:
	python -m mypy ./ --exclude '(__pycache__|venv)' --ignore-missing-imports
pylint:
	python -m pylint ./ --ignore venv,__pycache__ --recursive=true --disable=E0401,w0703
# build:
# 	@read -p "Tag?: " tag \
# 	&& docker login -u "gitlab-prixtips" -p "9foQyJKx3Mz6isyr_kN2" registry.aputek.com \
# 	&& docker buildx create --use \
# 	&& docker buildx build -f ./Dockerfile -t registry.aputek.com/prixtips/queue-checker:$$tag --platform linux/arm64 . --push
# unitest:
# 	pytest
