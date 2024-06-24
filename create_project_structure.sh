# Define the base directory
BASE_DIR="secure_file_sharing"

# Create the base directory
mkdir -p $BASE_DIR

# Create subdirectories
mkdir -p $BASE_DIR/alembic/versions
mkdir -p $BASE_DIR/app/routers
mkdir -p $BASE_DIR/migrations/versions
mkdir -p $BASE_DIR/tests

# Create __init__.py files to make Python recognize these directories as packages
touch $BASE_DIR/app/__init__.py
touch $BASE_DIR/app/routers/__init__.py
touch $BASE_DIR/tests/__init__.py

# Create initial main files
touch $BASE_DIR/app/main.py
touch $BASE_DIR/app/models.py
touch $BASE_DIR/app/schemas.py
touch $BASE_DIR/app/crud.py
touch $BASE_DIR/app/deps.py
touch $BASE_DIR/app/security.py

# Create initial router files
touch $BASE_DIR/app/routers/auth.py
touch $BASE_DIR/app/routers/files.py

# Create alembic configuration file
touch $BASE_DIR/alembic.ini

# Create .env file for environment variables
touch $BASE_DIR/.env

# Print the directory structure
echo "Created directory structure:"
tree $BASE_DIR
