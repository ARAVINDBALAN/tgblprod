import sqlite3

def priority(truck_value, machine_value, balance_to_do, ttc):
    connection = sqlite3.connect("pulp.db")
    db = connection.cursor()
    a = truck_value
    b = machine_value
    w3 = balance_to_do
    w4 = ttc

