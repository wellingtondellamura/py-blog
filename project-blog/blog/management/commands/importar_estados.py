from django.core.management import BaseCommand

class Command(BaseCommand):

    help = 'Importa os estados do arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        import csv
        from blog.models import City, State

        # Carregando os estados em um dicionario
        filename = options['filename'][0]


        states = list()
        with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                state = dict()
                state['id'] = row.get('codigo_uf')
                state['initials'] = row.get('uf')
                state['name'] = row.get('nome')
                states.append(state)

        for state in states:
            _, c = State.objects.get_or_create(id=state['id'], initials=state['initials'], name=state['name'])
            if (c):
                self.stdout.write(self.style.SUCCESS('Estado %s importado com sucesso' % state['name']))
            else:
                self.stdout.write(self.style.ERROR('Erro ao importar o estado %s. Já cadastrado' % state['name']))
            
