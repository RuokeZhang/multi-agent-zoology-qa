```python
"""
Simple evaluation harness for routing, citations, and answer presence.
"""
from agents import RouterAgent, ZoologyKnowledgeAgent, ClarifierAgent
from benchmark import BENCHMARK_QUESTIONS


def evaluate():
    router = RouterAgent()
    zoo_agent = ZoologyKnowledgeAgent()
    clarifier = ClarifierAgent()

    results = []
    for item in BENCHMARK_QUESTIONS:
        q = item["question"]
        expected = item["expected_agent"]
        clarifications = clarifier.check(q)
        if clarifications:
            routed = "ClarifierAgent"
        else:
            routed = router.route(q)
        answer, sources = zoo_agent.answer(q)
        passed_route = routed == expected
        has_citation = bool(sources) if item["must_cite"] else True
        results.append(
            {
                "id": item["id"],
                "question": q,
                "routed": routed,
                "expected": expected,
                "route_ok": passed_route,
                "has_citation": has_citation,
                "answer_present": bool(answer),
            }
        )
    return results


if __name__ == "__main__":
    # TODO: Expand metrics and reporting
    import json
    res = evaluate()
    print(json.dumps(res, indent=2))
```
