```python
from flask import Flask, request, jsonify, render_template
from agents import (
    RouterAgent,
    ZoologyKnowledgeAgent,
    ClarifierAgent,
    ImageHintAgent,
    CurriculumAgent,
    TerminologyAgent,
    SessionMemoryAgent,
)
from benchmark import BENCHMARK_QUESTIONS
import time

app = Flask(__name__)

router = RouterAgent()
zoo_agent = ZoologyKnowledgeAgent()
clarifier = ClarifierAgent()
image_hint_agent = ImageHintAgent()
curriculum_agent = CurriculumAgent()
terminology_agent = TerminologyAgent()
session_memory = SessionMemoryAgent()

recent_logs = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json or {}
    question = data.get("question", "").strip()
    session_id = data.get("session_id", "default")
    image_url = data.get("image_url")
    age_level = data.get("age_level")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    session_memory.remember(session_id, question)
    route = router.route(question)
    clarifications = clarifier.check(question)
    if clarifications:
        response = {
            "agent": "ClarifierAgent",
            "clarifications": clarifications,
            "answer": "I need more details before answering."
        }
    else:
        if image_url:
            image_hint = image_hint_agent.suggest_species(image_url)
        else:
            image_hint = None
        answer, sources = zoo_agent.answer(question, image_hint=image_hint)
        if age_level:
            answer = curriculum_agent.rewrite(answer, age_level=age_level)
        glossary = terminology_agent.glossary(question)
        response = {
            "agent": route,
            "answer": answer,
            "sources": sources,
            "glossary": glossary,
            "image_hint": image_hint,
            "memory": session_memory.get_context(session_id),
        }

    log_entry = {
        "ts": time.time(),
        "question": question,
        "route": route,
        "response_agent": response.get("agent"),
        "sources": response.get("sources"),
    }
    recent_logs.append(log_entry)
    recent_logs[:] = recent_logs[-50:]

    return jsonify(response)


@app.route("/admin/debug")
def admin_debug():
    return jsonify({"recent": recent_logs, "benchmark_size": len(BENCHMARK_QUESTIONS)})


@app.route("/api/benchmark")
def api_benchmark():
    return jsonify({"benchmark": BENCHMARK_QUESTIONS})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
```
