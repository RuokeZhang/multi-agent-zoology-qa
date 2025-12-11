```python
BENCHMARK_QUESTIONS = [
    {
        "id": "q1",
        "question": "What is the conservation status of the African elephant?",
        "expected_agent": "conservation_expert",
        "must_cite": True,
    },
    {
        "id": "q2",
        "question": "Describe the social behavior of meerkats.",
        "expected_agent": "behavior_expert",
        "must_cite": True,
    },
    {
        "id": "q3",
        "question": "Is the emperor penguin endothermic?",
        "expected_agent": "physiology_expert",
        "must_cite": False,
    },
    {
        "id": "q4",
        "question": "How does deforestation affect orangutan ecology?",
        "expected_agent": "ecology_expert",
        "must_cite": True,
    },
    {
        "id": "q5",
        "question": "Clarify: does it migrate south?",
        "expected_agent": "ClarifierAgent",
        "must_cite": False,
    },
]
```
