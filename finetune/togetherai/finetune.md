# Prepare Rust Code Data

Datasets must be [JSONL](https://jsonlines.org/) files. Each line should be formatted with a single "text" field, like this:

JSONL

```Text
{"text": "use super::*;\n\nuse crate::Flags;\n\n#[test]\nfn cases() {\n ..."}
{"text": "..."}
{"text": "..."}
```

# Finetune on together.ai

To get started, install the `together` Python library:

```shell
pip install --upgrade together
```

Then, configure your API key by setting the `TOGETHER_API_KEY` environment variable (see [this section](https://docs.together.ai/docs/get-started#api-key) for instructions on how to get your API key). You can configure this in an initialization script or by running this command:

```shell
export TOGETHER_API_KEY="<TOGETHER-API-KEY>"
```

### Upload data files

Now that you've prepared your dataset, upload it with:

```shell
together files upload <FILENAME>
```

### Start fine-tuning

Once you've uploaded your dataset, copy your file id from the output above and select a base model to fine-tune. Check out the [full model list](https://docs.together.ai/docs/models-fine-tuning) available for fine-tuning.

Run the following command to start your fine-tuning job:

```Text
together finetune create -t <FILE-ID> -m <MODEL-NAME>
```