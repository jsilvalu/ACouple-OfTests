import json

import pytest
import requests


class TestClass:

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test1(self):
        URL = "http://localhost:5000/api/2.0.0/sports"
        username = "3ntr3v1st4"
        password = "t3cn1c4"

        # Authentication with username and password
        response = requests.get(URL, auth=(username, password))
        assert response.status_code == 200
        assert response.json() == {'cycling': {'sportsman': [
            {'name': 'Alejandro Valverde', 'order': '0', 'specialty': 'all', 'team_id': 'MVS', 'type': 'road'},
            {'name': 'Peter Sagan', 'order': '1', 'specialty': 'sprinter', 'team_id': 'TEN', 'type': 'road'},
            {'name': 'Filippo Ganna', 'order': '2', 'specialty': 'persecution', 'team_id': 'IGD', 'type': 'track'},
            {'name': 'Wout van Aert', 'order': '3', 'specialty': 'worldraces', 'team_id': 'TJV', 'type': 'ciclocross'}],
            'teams': [{'id': 'MVS', 'order': '0', 'value': 'Movistar'},
                      {'id': 'TEN', 'order': '1', 'value': 'Team TotalEnergies'},
                      {'id': 'IGD', 'order': '2', 'value': 'INEOS GRENADIERS'},
                      {'id': 'TJV', 'order': '4', 'value': 'Jumbo-Visma'}]},
            'football': {'sportsman': [
                {'name': 'Luis Alfonso Espino García', 'order': 0, 'specialty': 'Defender',
                 'team_id': 'CDZ', 'type': 'fieldplayer'},
                {'name': 'Brian Oliván', 'order': 1, 'specialty': 'lateralizdo',
                 'team_id': 'MLLRC', 'type': 'fieldplayer'},
                {'name': 'Oihan Sancet Tirapu', 'order': 2, 'specialty': 'Midfielder',
                 'team_id': 'ATC', 'type': 'fieldplayer'},
                {'name': 'Jaume Doménech', 'order': 3, 'specialty': 'Goalkeeper',
                 'team_id': 'VCF', 'type': 'Goalkeeper'}],
                'teams': [{'id': 'CDZ', 'order': 0, 'value': ''},
                          {'id': 'MLLRC', 'order': 1,
                           'value': 'Real Club Deportivo Mayorca'},
                          {'id': 'ATC', 'order': 2, 'value': 'ATHLETIC CLUB DE BILBAO'},
                          {'id': 'VCF', 'order': 3,
                           'value': 'Valencia Club de Fútbol'}]}, 'type': 'full',
            'version': '2.0.0'}

        endpoint = "/cycling"
        response = requests.get(URL + endpoint, auth=(username, password))
        sportsman = response.json()["cycling"]["sportsman"]
        teams = response.json()["cycling"]["teams"]

        assert len(sportsman) == len(teams)


        my_dict = {}

        for i in response.json()["cycling"]["sportsman"]:
            my_dict[i["name"]] = i['team_id']

        print(my_dict)
