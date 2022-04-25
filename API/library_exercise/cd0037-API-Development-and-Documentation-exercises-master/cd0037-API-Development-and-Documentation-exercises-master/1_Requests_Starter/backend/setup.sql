DROP DATABASE IF EXISTS bookshelf;
DROP DATABASE IF EXISTS bookshelf_test;
DROP USER IF EXISTS student2;
CREATE DATABASE bookshelf;
CREATE DATABASE bookshelf_test;
CREATE USER student2 WITH ENCRYPTED PASSWORD 'student';
GRANT ALL PRIVILEGES ON DATABASE bookshelf TO student2;
GRANT ALL PRIVILEGES ON DATABASE bookshelf_test TO student2;
ALTER USER student2 CREATEDB;
ALTER USER student2 WITH SUPERUSER;