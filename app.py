# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
import requests  
# creating a Flask app 
app = Flask(__name__) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
  
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/validators/', methods = ['GET']) 
def getValidator():
    jailed = False
    if request.args['jailed'] == 'true':
        jailed = True
    res = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/validators').json()
    data = []
    staked_token = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/pool').json()['pool']['bonded_tokens']
    for i, each in enumerate(res['validators']):
        temp = {}
        print(each['jailed'],jailed, each['jailed'] == jailed)
        if each['jailed'] == jailed:
            print('http://18.117.74.150:1317/cosmos/distribution/v1beta1/validators/{}'.format(each['operator_address']))
            rewardsandcommision = requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/validators/{}'.format(each['operator_address'])).json()
            reward = 0 
            if len(rewardsandcommision['self_bond_rewards']) > 0 : 
                reward = rewardsandcommision['self_bond_rewards'][0]['amount']
            commission = 0 
            if len(rewardsandcommision['commission']) > 0 : 
                commission = rewardsandcommision['commission'][0]['amount']
            temp = {
                "id": i+1,
                "delegator": each['operator_address'],
                "address": each['operator_address'],
                "cons_address": each['consensus_pubkey']['key'],
                "moniker": each['description']['moniker'],
                "website": each['description']['website'],
                "identity": each['description']['identity'],
                "contacts": each['description']['security_contact'],
                "details": each['description']['details'],
                "rate": each['commission']['commission_rates']['rate'],
                "max_rate": each['commission']['commission_rates']['max_rate'],
                "max_change_rate": each['commission']['commission_rates']['max_change_rate'],
                "min_self_delegation": each['min_self_delegation'],
                "stake": each['tokens'],
                "rewards": reward,
                "commissions": commission,
                "voting_power": int(int(staked_token)/int(each['tokens'])),
                "jailed": jailed
            }
            data.append(temp)
    data = sorted(data, key=lambda k: k['stake'], reverse=True)
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/validators/<string:validator_address>', methods = ['GET']) 
def getValidatorById(validator_address):
    each = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/validators/{}'.format(validator_address)).json()['validator']
    rewardsandcommision = requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/validators/{}'.format(validator_address)).json()
    staked_token = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/pool').json()['pool']['bonded_tokens']
    temp = {
        "id": each['operator_address'],
        "delegator": each['operator_address'],
        "address": each['operator_address'],
        "cons_address": each['consensus_pubkey']['key'],
        "moniker": each['description']['moniker'],
        "website": each['description']['website'],
        "identity": each['description']['identity'],
        "contacts": each['description']['security_contact'],
        "details": each['description']['details'],
        "rate": each['commission']['commission_rates']['rate'],
        "max_rate": each['commission']['commission_rates']['max_rate'],
        "max_change_rate": each['commission']['commission_rates']['max_change_rate'],
        "min_self_delegation": each['min_self_delegation'],
        "stake": each['tokens'],
        "rewards": rewardsandcommision['self_bond_rewards'][0]['amount'],
        "commissions": rewardsandcommision['commission'][0]['amount'],
        "voting_power": int(int(staked_token)/int(each['tokens'])),
        "jailed": False
    }
    
    response = jsonify(temp)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response



# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/validators/<string:validator_address>/delegators/', methods = ['GET']) 
def getValidatorDelegationById(validator_address):
    res = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/validators/{}/delegations'.format(validator_address)).json()['delegation_responses']
    data = []
    for each in res:
        data.append({"delegator": each['delegation']['delegator_address'], "amount": each['delegation']['shares'].split('.')[0]})

    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/validators/count', methods = ['GET']) 
def getValidatorCount():
    data = {
        "active": 0,
        "inactive": 0,
        "jailed": 0,
        "total": 0
    }
    res = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/validators').json()
    data['total'] = len(res['validators'])
    staked_token = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/pool').json()['pool']['bonded_tokens']
    for i, each in enumerate(res['validators']):
        temp = {}
        if each['jailed'] == True:
            data['jailed'] +=1
    print(data)
    data['active']  = len(res['validators']) - int(data['jailed'])
        
    return jsonify(data)
  

# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/head/', methods = ['GET']) 
def getHead():
    data = {
        "id": 1,
        "name": "celestia_indexer",
        "chain_id": "self-1",
        "last_height": 1207724,
        "hash": "99c912bb68a1a074b9133dc20de01b5d954ac0cf923b6bc41094683a415ea4bc",
        "last_time": "2024-06-09T06:09:28.039514Z",
        "total_tx": 514490,
        "total_accounts": 3692,
        "total_fee": "213956977799",
        "total_blobs_size": 14212278774,
        "total_validators": 4,
        "total_supply": "1034769972591238",
        "total_stake": "399999980900080",
        "total_voting_power": "300000000",
        "synced": true
    }

    res = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/validators').json()
    data['total'] = len(res['validators'])
    staked_token = requests.get('http://18.117.74.150:1317/cosmos/staking/v1beta1/pool').json()['pool']['bonded_tokens']
    for i, each in enumerate(res['validators']):
        temp = {}
        if each['jailed'] == True:
            data['jailed'] +=1
    print(data)
    data['active']  = len(res['validators']) - int(data['jailed'])
        
    return jsonify({'data': data})
  

def generate_consensus_config():
    data = requests.get('http://18.117.74.150:1317/cosmos/consensus/v1/params').json()['params']
    return {
        "block_max_bytes": data['block']['max_bytes'],
        "block_max_gas": data['block']['max_gas'],
        "evidence_max_age_duration": data['evidence']['max_age_duration'],
        "evidence_max_age_num_blocks": data['evidence']['max_age_num_blocks'],
        "evidence_max_bytes": data['evidence']['max_bytes'],
        "validator_pub_key_types": data['validator']['pub_key_types']
    }



# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/constants/', methods = ['GET']) 
def getConstants():
    data = {
        "module": {
            "auth": requests.get('http://18.117.74.150:1317/cosmos/auth/v1beta1/params').json()['params'],
            "blob": {
                    "gas_per_blob_byte": "8",
                    "gov_max_square_size": "64"
                },
            "consensus": generate_consensus_config(),
            "crisis": {
                    "constant_fee": "1000uSLF"
                },
            "distribution": requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/params').json()['params'],
            "gov": requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/params').json()['params'],
            "slashing": requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/params').json()['params'],
            "staking": requests.get('http://18.117.74.150:1317/cosmos/distribution/v1beta1/params').json()['params']
        },
        "denom_metadata": [
            {
                "description": "The native token of the Self Chain.",
                "base": "uslf",
                "display": "SLF",
                "name": "SLF",
                "symbol": "SLF",
                "uri": "",
                "units": [
                    {
                        "denom": "uslf",
                        "exponent": 0,
                        "aliases": [
                            "microslf"
                        ]
                    },
                    {
                        "denom": "SLF",
                        "exponent": 6,
                        "aliases": []
                    }
                ]
            }
        ]

    }

    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
  



  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 
