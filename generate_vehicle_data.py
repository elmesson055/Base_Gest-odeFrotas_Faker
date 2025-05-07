import pandas as pd
from faker import Faker
import random
import datetime

fake = Faker('pt_BR')

# Helper functions
def random_date(start, end):
    return fake.date_between(start_date=start, end_date=end)

def random_float(min_val, max_val, decimals=2):
    return round(random.uniform(min_val, max_val), decimals)

# Constants
vehicle_types = ['Caminhão', 'Carro', 'Carreta']
colors = ['Preto', 'Branco', 'Prata', 'Vermelho', 'Azul', 'Verde', 'Amarelo']
situations = ['Ativo', 'Inativo', 'Vendido', 'Roubado']
fuel_types = ['Gasolina', 'Etanol', 'Diesel', 'GNV']
departments = ['Logística', 'Vendas', 'Manutenção', 'Diretoria']

# Lists to store data
main_data = []
maintenance_history = []
fuel_control = []
fines = []

for i in range(10000):
    vehicle_id = f"V{i+1:05d}"
    plate = fake.license_plate()
    brand = fake.company()
    model = fake.word().capitalize()
    year_fab = random.randint(2000, 2023)
    year_model = year_fab + random.randint(0, 2)
    vtype = random.choice(vehicle_types)
    color = random.choice(colors)
    chassi = fake.bothify(text='?????????????????')
    renavam = fake.numerify(text='###########')
    acquisition_date = random_date('-10y', 'today')
    purchase_value = random_float(20000, 200000)
    situation = random.choice(situations)
    driver = fake.name()
    department = random.choice(departments)
    last_use_date = random_date(acquisition_date, 'today')
    km = random.randint(0, 300000)
    horimeter = random.randint(0, 8000) if vtype == 'Caminhão' else None

    # Maintenance
    last_maintenance = random_date(acquisition_date, 'today')
    next_maintenance = last_maintenance + datetime.timedelta(days=random.randint(30, 365))
    maintenance_type = random.choice(['Preventiva', 'Corretiva', 'Revisão'])
    maintenance_cost = random_float(500, 5000)
    maintenance_provider = fake.company()
    # Add to maintenance history
    maintenance_history.append({
        'ID Veículo': vehicle_id,
        'Data': last_maintenance,
        'Tipo': maintenance_type,
        'Custo': maintenance_cost,
        'Fornecedor': maintenance_provider
    })

    # Insurance, IPVA, Licensing
    insurance_value = random_float(1000, 5000)
    insurance_validity = last_maintenance + datetime.timedelta(days=365)
    ipva_status = random.choice(['Pago', 'Pendente'])
    ipva_validity = last_maintenance + datetime.timedelta(days=365)
    licensing_validity = last_maintenance + datetime.timedelta(days=365)

    # Fuel
    last_fuel_date = random_date(acquisition_date, 'today')
    fuel_type = random.choice(fuel_types)
    last_fuel_km = random.randint(0, km)
    liters = random_float(10, 80)
    cost_per_liter = random_float(4, 8)
    avg_consumption = random_float(5, 15)
    # Add to fuel control
    fuel_control.append({
        'ID Veículo': vehicle_id,
        'Data Abastecimento': last_fuel_date,
        'Tipo Combustível': fuel_type,
        'Quilometragem': last_fuel_km,
        'Litros': liters,
        'Custo por Litro': cost_per_liter,
        'Média Consumo (Km/L)': avg_consumption
    })

    # Accessories/Observations
    accessories = ', '.join(fake.words(nb=random.randint(0, 3)))
    observations = fake.sentence()

    # Fines
    if random.random() < 0.1:  # 10% chance of fine
        fine_date = random_date(acquisition_date, 'today')
        fine_value = random_float(100, 3000)
        fines.append({
            'ID Veículo': vehicle_id,
            'Data': fine_date,
            'Valor': fine_value
        })

    # Main data
    main_data.append({
        'ID Veículo': vehicle_id,
        'Placa': plate,
        'Marca': brand,
        'Modelo': model,
        'Ano Fabricação': year_fab,
        'Ano Modelo': year_model,
        'Tipo': vtype,
        'Cor': color,
        'Chassi': chassi,
        'Renavam': renavam,
        'Data Aquisição': acquisition_date,
        'Valor Compra': purchase_value,
        'Situação': situation,
        'Motorista': driver,
        'Departamento': department,
        'Data Última Utilização': last_use_date,
        'Quilometragem Atual': km,
        'Horímetro': horimeter,
        'Última Revisão': last_maintenance,
        'Próxima Revisão': next_maintenance,
        'Tipo Última Manutenção': maintenance_type,
        'Custo Última Manutenção': maintenance_cost,
        'Fornecedor Manutenção': maintenance_provider,
        'Seguro Valor': insurance_value,
        'Seguro Validade': insurance_validity,
        'IPVA Status': ipva_status,
        'IPVA Validade': ipva_validity,
        'Licenciamento Validade': licensing_validity,
        'Data Último Abastecimento': last_fuel_date,
        'Tipo Combustível': fuel_type,
        'Última Km Abastecida': last_fuel_km,
        'Litros Abastecidos': liters,
        'Custo por Litro': cost_per_liter,
        'Média Consumo (Km/L)': avg_consumption,
        'Acessórios': accessories,
        'Observações': observations
    })

# Convert to DataFrames
df_main = pd.DataFrame(main_data)
df_maintenance = pd.DataFrame(maintenance_history)
df_fuel = pd.DataFrame(fuel_control)
df_fines = pd.DataFrame(fines)

# Save to Excel with multiple sheets
with pd.ExcelWriter('c:\\Users\\elmessonjesus\\Desktop\\Base\\veiculos.xlsx') as writer:
    df_main.to_excel(writer, sheet_name='Principal', index=False)
    df_maintenance.to_excel(writer, sheet_name='Manutencoes', index=False)
    df_fuel.to_excel(writer, sheet_name='Abastecimento', index=False)
    df_fines.to_excel(writer, sheet_name='Multas', index=False)