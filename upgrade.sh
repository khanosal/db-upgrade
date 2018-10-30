#!/bin/bash


die() {
    printf '%s\n' "$1" >&2
    exit 1
}


# directory-with-sql-scripts username-for-the-db db-host db-name db-password
while :; do
    case $1 in
        -h|-\?|--help)
            usage   # Display a usage synopsis.
            exit
            ;;
        -d|--directory-with-sql-scripts)  # Takes an option argument; ensure it has been specified.
            if [ "$2" ]; then
                directory_with_sql_scripts=$2
                shift
            else
                die 'ERROR: "--directory-with-sql-script" requires a non-empty option argument.'
            fi
            ;;
        --directory-with-sql-scripts=?*)
            directory_with_sql_scripts=${1#*=} # Delete everything up to "=" and assign the remainder.
            ;;
        --directory-with-sql-scripts=)  # Handle the case of an empty --directory-with-sql-scripts=
            die 'ERROR: "--file" requires a non-empty option argument.'
            ;;
        --)              # End of all options.
            shift
            break
            ;;
        -?*)
            printf 'WARN: Unknown option (ignored): %s\n' "$1" >&2
            ;;
        *)               # Default case: No more options, so break out of the loop.
            break
    esac
		case $3 in
        -u|--username-for-the-db)  # Takes an option argument; ensure it has been specified.
            if [ "$4" ]; then
                username-for-the-db=$4
                shift
            else
                die 'ERROR: "--directory-with-sql-script" requires a non-empty option argument.'
            fi
            ;;
        --username-for-the-db=?*)
            username-for-the-db=${3#*=} # Delete everything up to "=" and assign the remainder.
            ;;
        --username-for-the-db=)  # Handle the case of an empty --directory-with-sql-scripts=
            die 'ERROR: "--username-for-the-db" requires a non-empty option argument.'
            ;;
        --)              # End of all options.
            shift
            break
            ;;
        -?*)
            printf 'WARN: Unknown option (ignored): %s\n' "$3" >&4
            ;;
        *)               # Default case: No more options, so break out of the loop.
            break
    esac
    shift

done

echo directory_with_sql_scripts
echo username-for-the-db


# Rest of the program here.
# If there are input files (for example) that follow the options, they
# will remain in the "$@" positional parameters.

function usage()
{
	echo "Usage : $0 [-a <option>][-c <option>]"
}
