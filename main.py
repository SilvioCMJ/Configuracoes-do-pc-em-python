import wmi

#importano lib
w = wmi.WMI()
pc = w.Win32_ComputerSystem()[0]

#exibindo resultado
print(f'Marca: {pc.Manufacturer}')
print(f'Modelo: {pc.Model}')
print(f'Nome: {pc.Name}')
print(f'Numero de cpus: {pc.NumberOfProcessors}')
print(f'Arquitetura: {pc.SystemType}')
