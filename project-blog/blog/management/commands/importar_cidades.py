from django.core.management import BaseCommand

class Command(BaseCommand):


    help = 'Importa as cidades do arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
        parser.add_argument('output', type=bool, default=False, nargs='?')


    def handle(self, *args, **options):
        import csv

        from blog.models import City, State
        filename = options['filename']
        output = True if options['output'] else False
        cities = list()
        with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                city = dict()
                city['state'] = State.objects.get(id=row.get('codigo_uf'))
                city['name'] = row.get('nome')
                cities.append(city)

        # Inserindo os dados no model Cidade
        for city in cities:
            c = City.objects.get_or_create(name=city['name'], state=city['state'])
            if (output):
                if (c != None):
                    self.stdout.write(self.style.SUCCESS('Cidade %s importada com sucesso' % city['name']))
                else:
                    self.stdout.write(self.style.ERROR('Erro ao importar a cidade %s. Já cadastrada' % city['name']))
