# Visit preparation workspace

An independent implementation demonstration by Shaunak Mali, inspired by Metriport's data integration workflows. Not an official Metriport product.

Start with the guided walkthrough, then choose **Explore the full patient workspace**. Review a synthetic longitudinal chart, inspect source records, reconcile deliberately conflicting information, and prepare a handoff. Light and dark themes are available. Browser-local changes can be reset.

## What this demonstrates

- Appointment-driven preparation and source-linked chart review.
- Trends and clinical record navigation with evidence visible alongside findings.
- Missing information and data conflicts that require human review.
- A guided handoff and a proposed special-projects ownership plan.

All patient records in this repository were authored as synthetic fixtures. No private CRM, email, transcript, credentials, or cached patient response is included. The application does not contact Metriport, retrieve live patient information, write to an EHR, or provide validated clinical recommendations. The guided walkthrough and full workspace are separate demonstrations; their state does not synchronize.

## Run locally

Requires Python 3.12 or a compatible Python 3 installation. No third-party dependencies.

```sh
python3 server.py
```

Open http://127.0.0.1:8795. Only explicit public assets and the authored fixture endpoint are served. POST requests are disabled. Browser state stays on the device.

## Railway deployment preparation

The Dockerfile and railway.toml define a standalone service with `/health` as its health check. Railway supplies PORT and RAILWAY_ENVIRONMENT_ID. Only in that hosted environment does the server bind to the container's public interface. Local execution binds to loopback.

Deploy only this directory, never the parent CRM directory. No volume, database, API key, or external service is required. Create a dedicated Railway project and service, upload this reviewed directory using the Railway CLI, and generate a public domain. Do not connect automatic GitHub deployments without separate approval.

Publication and deployment require the owner's approval for the exact prepared version and target. The repository and hosting service have not been published by this preparation.

## Sources and limitations

The interface links to the Metriport Sollis Health customer story, public medication reference resources, and design research. Those are contextual references, not evidence that this demonstration has been clinically validated. Deliberate fixture inconsistencies demonstrate reconciliation, not patient-care advice. No official logo is distributed. Deployment health checks establish process readiness, not clinical correctness.
