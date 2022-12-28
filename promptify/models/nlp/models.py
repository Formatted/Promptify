import openai


class GPT3:
    def __init__(self, api_key):
        self._api_key = api_key
        self._openai = openai
        self._openai.api_key = openai.api_key = self._api_key

    def get_model_list(self):
        list_of_models = [model.id for model in self._openai.Model.list()['data']]
        return list_of_models

    def prompt_model_generation(self,
                                model_name=None,
                                prompts=None,
                                temperature=0,
                                max_tokens=6,
                                top_p=0.1,
                                frequency_penalty=0,
                                presence_penalty=0,
                                stop=None,
                                multiple=False
                                ):
        if multiple:
            result = []
            for prompt in prompts:
                response = self._openai.Completion.create(
                    model=model_name,
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty,
                    stop=stop
                )
                result.append(response['choices'][0]['text'])

        else:
            response = self._openai.Completion.create(
                model=model_name,
                prompt=prompts,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop
            )
            result = response['choices'][0]['text']
        return result