# database-backup-ui
A simple cross-platform database backup tool with UI built using Flet. Supports MySQL and PostgreSQL.
# Database Backup Tool (Flet)

A simple desktop application to backup MySQL and PostgreSQL databases with a graphical interface built using [Flet](https://flet.dev/).

## Features
- Backup MySQL and PostgreSQL databases
- Choose custom folder for saving backups
- User-friendly UI
- Auto-generate backup file names with date

## Usage
1. Select database type (MySQL / PostgreSQL)
2. Enter host, user, password, and database name
3. Choose a folder to save the backup
4. Click **Backup** 🎉

## Requirements
- Python 3.9+
- Flet
- mysqldump (for MySQL)
- pg_dump (for PostgreSQL)
