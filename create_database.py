import sqlite3
import pandas as pd

# Create a database
conn = sqlite3.connect('database.db')

# Load csv data
visits = pd.read_csv('data/visits.csv')
fitness_tests = pd.read_csv('data/fitness_tests.csv')
applications = pd.read_csv('data/applications.csv')
purchases = pd.read_csv('data/purchases.csv')

# Add the data to our database
visits.to_sql('visits', conn, dtype={
    'first_name': 'VARCHAR(256)',
    'last_name': 'VARCHAR(256)',
    'email': 'VARCHAR(256)',
    'gender': 'VARCHAR(256)',
    'visit_date': 'DATE'
})

fitness_tests.to_sql('fitness_tests', conn, dtype={
    'first_name': 'VARCHAR(256)',
    'last_name': 'VARCHAR(256)',
    'email': 'VARCHAR(256)',
    'gender': 'VARCHAR(256)',
    'fitness_test_date': 'DATE'
})

applications.to_sql('applications', conn, dtype={
    'first_name': 'VARCHAR(256)',
    'last_name': 'VARCHAR(256)',
    'email': 'VARCHAR(256)',
    'gender': 'VARCHAR(256)',
    'application_date': 'DATE'
})

purchases.to_sql('purchases', conn, dtype={
    'first_name': 'VARCHAR(256)',
    'last_name': 'VARCHAR(256)',
    'email': 'VARCHAR(256)',
    'gender': 'VARCHAR(256)',
    'purchases_date': 'DATE'
})
