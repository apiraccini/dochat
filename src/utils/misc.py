import tiktoken

def estimate_cost(messages, model='gpt-3.5-turbo', max_tokens=512):

    encoding = tiktoken.encoding_for_model(model)
    tokens_per_message = 3
    tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3

    if model == 'gpt-3.5-turbo':
        cost_per_input_token = 0.0015 / 1000
        cost_per_output_token = 0.002 / 1000
    elif model == 'gpt-3.5-turbo-16k':
        cost_per_input_token = 0.003 / 1000
        cost_per_output_token = 0.004 / 1000
    elif model == 'gpt-4':
        cost_per_input_token = 0.03 / 1000
        cost_per_output_token = 0.06 / 1000

    cost_estimate = num_tokens*cost_per_input_token + max_tokens*cost_per_output_token
    
    return num_tokens, cost_estimate
