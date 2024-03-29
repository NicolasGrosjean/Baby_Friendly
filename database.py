import json
import logging
import os
import overpass

logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


class Database:
    def __init__(self, expressions, bbox):
        """
        Extract with overpass corresponding OSM data according expressions in the boundingg box.
        :param expressions:
        :param bbox:
        """
        query = '('
        for expr in expressions:
            query += 'node[' + expr + '](' + bbox + ');'
            query += 'way[' + expr + '](' + bbox + ');'
            query += 'relation[' + expr + '](' + bbox + ');'
        query += ')'

        logging.info('Call Overpass to extract data')
        api = overpass.API(endpoint='http://overpass-api.de/api/interpreter')
        response = api.get(query, verbosity='geom')
        self.osm_data = response['features']
        with open(os.path.join('data', 'overpass_data.geojson'), 'w') as outfile:
            json.dump(self.osm_data, outfile)
        logging.info('Data extracted from Overpass')

    def add_additional_osm_data(self, additional_node_ids, additional_way_ids, bbox):
        query = '('
        for node_id in additional_node_ids:
            query += 'node(' + str(node_id) + ')(' + bbox + ');'
        for way_id in additional_way_ids:
            query += 'way(' + str(way_id) + ')(' + bbox + ');'
        query += ')'

        logging.info('Call Overpass to extract additional data')
        api = overpass.API(endpoint='http://overpass-api.de/api/interpreter')
        response = api.get(query, verbosity='geom')
        for elem in response['features']:
            self.osm_data.append(elem)
        logging.info('Additional data extracted from Overpass')

    def merge_with_external_data(self, filepath):
        with open(filepath) as f:
            data = json.load(f)
        for ext_elem in data:
            for osm_elem in self.osm_data:
                if ext_elem['id'] == osm_elem['id']:
                    for key, value in ext_elem['properties'].items():
                        osm_elem['properties'][key] = value
                    break

    def export_to_geojson(self, filters):
        for or_filter in filters:
            filtered_elems = []
            for elem in self.osm_data:
                for key, value in or_filter.items():
                    if key in elem['properties'] and (value is None or elem['properties'][key] == value):
                        filtered_elems.append(elem)
            filter_name = list(or_filter.items())[0][0]
            if list(or_filter.items())[0][1] is not None and list(or_filter.items())[0][1] != 'yes':
                filter_name += '_' + list(or_filter.items())[0][1]
            with open(os.path.join('data', filter_name + '.geojson'), 'w') as outfile:
                json.dump(filtered_elems, outfile)
        logging.info('Geojson files exported')


if __name__ == '__main__':
    bbox = '45.1416, 5.6732, 45.2270, 5.7826'

    db = Database(['diaper=yes', 'changing_table=yes', 'highchair',
                   'amenity=kindergarten]["school:FR"!=maternelle',
                   'leisure=playground'], bbox)

    additional_nodes = [616882177, 6637704290, 6640117127]
    additional_ways = [42208752]
    db.add_additional_osm_data(additional_nodes, additional_ways, bbox)
    db.merge_with_external_data(os.path.join('data', 'non_osm_data.geojson'))
    db.export_to_geojson([{'diaper': 'yes', 'changing_table': 'yes'}, {'highchair': None}, {'microwave': 'yes'},
                          {'calm': 'yes'}, {'toys': 'yes'}, {'stroller_parking': 'yes'}, {'amenity': 'kindergarten'},
                          {'leisure': 'playground'}])
