import { useState } from "react";
import "./index.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const API_URL = "https://ai-resume-matcher-9peg.onrender.com";

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a PDF resume first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/upload-resume`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to analyze resume.");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      alert("Something went wrong. Please try again.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <section className="mx-auto flex min-h-screen max-w-6xl flex-col items-center justify-center px-6 py-12">
        <div className="mb-10 text-center">
          <span className="rounded-full border border-cyan-400/40 bg-cyan-400/10 px-4 py-2 text-sm text-cyan-300">
            AI Resume Matcher
          </span>

          <h1 className="mt-6 text-4xl font-bold tracking-tight sm:text-6xl">
            Analyze resumes with{" "}
            <span className="text-cyan-400">Machine Learning</span>
          </h1>

          <p className="mx-auto mt-5 max-w-2xl text-slate-300">
            Upload a PDF resume and get an instant suitability prediction using
            a FastAPI backend, skill extraction, and a Random Forest model.
          </p>
        </div>

        <div className="grid w-full gap-6 md:grid-cols-2">
          <form
            onSubmit={handleSubmit}
            className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-2xl"
          >
            <h2 className="text-2xl font-semibold">Upload Resume</h2>
            <p className="mt-2 text-sm text-slate-400">
              PDF files only. Your resume will be analyzed by the deployed API.
            </p>

            <label className="mt-6 flex cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed border-cyan-400/40 bg-slate-900/70 p-8 text-center hover:border-cyan-300">
              <input
                type="file"
                accept="application/pdf"
                className="hidden"
                onChange={(e) => setFile(e.target.files[0])}
              />
              <span className="text-lg font-medium">
                {file ? file.name : "Choose a PDF resume"}
              </span>
              <span className="mt-2 text-sm text-slate-400">
                Click here to browse your file
              </span>
            </label>

            <button
              type="submit"
              disabled={loading}
              className="mt-6 w-full rounded-2xl bg-cyan-400 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? "Analyzing..." : "Analyze Resume"}
            </button>
          </form>

          <div className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-2xl">
            <h2 className="text-2xl font-semibold">Prediction Result</h2>
            <p className="mt-2 text-sm text-slate-400">
              The result will appear here after analysis.
            </p>

            {!result && (
              <div className="mt-8 rounded-2xl bg-slate-900/70 p-6 text-slate-400">
                No resume analyzed yet.
              </div>
            )}

            {result && (
              <div className="mt-8 space-y-5">
                <div className="rounded-2xl bg-slate-900/70 p-5">
                  <p className="text-sm text-slate-400">Prediction</p>
                  <p
                    className={`mt-2 text-3xl font-bold ${
                      result.prediction === "Suitable"
                        ? "text-emerald-400"
                        : "text-red-400"
                    }`}
                  >
                    {result.prediction}
                  </p>
                </div>

                <div className="rounded-2xl bg-slate-900/70 p-5">
                  <p className="text-sm text-slate-400">Confidence</p>
                  <p className="mt-2 text-3xl font-bold text-cyan-400">
                    {result.confidence}
                  </p>
                </div>

                <div className="rounded-2xl bg-slate-900/70 p-5">
                  <p className="text-sm text-slate-400">Detected Skills</p>
                  <div className="mt-4 flex flex-wrap gap-2">
                    {Object.entries(result.skills)
                      .filter(([_, value]) => value === 1)
                      .map(([skill]) => (
                        <span
                          key={skill}
                          className="rounded-full bg-cyan-400/10 px-3 py-1 text-sm text-cyan-300"
                        >
                          {skill.replaceAll("_", " ")}
                        </span>
                      ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;