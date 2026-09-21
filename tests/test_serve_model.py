import pytest

from experiments.serve_model import serve_model


def test_serve_model_refuses_unknown_model_key():
    with pytest.raises(SystemExit):
        serve_model("not-a-real-model")


def test_serve_model_refuses_non_local_vllm_model():
    # gpt-oss-120b is serving: external -- serve_model.py is only for
    # serving: local_vllm models; it should refuse before touching vLLM at all.
    with pytest.raises(SystemExit):
        serve_model("gpt-oss-120b")
