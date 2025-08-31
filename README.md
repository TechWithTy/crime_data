# Crime Data Integration (Provider-agnostic)

Proxies a provider-agnostic crime data API (e.g., SpotCrime-like) through our backend.

## Environment Variables

- CRIME_DATA_BASE_URL (required)
- CRIME_DATA_API_KEY (optional; used as Bearer in Authorization header)
- CRIME_DATA_TIMEOUT (default: 15)

Example .env:
CRIME_DATA_BASE_URL=https://api.your-crime-provider.com
# Optional
CRIME_DATA_API_KEY=your_key_here
CRIME_DATA_TIMEOUT=15

## Endpoints

- GET /crime-data/health
  - Returns: { healthy, base_url, has_api_key }

- GET /crime-data/{path}
  - Proxies GET to: {CRIME_DATA_BASE_URL}/{path}
  - Forwards query params verbatim.

Examples:
curl "http://localhost:8000/crime-data/health"

curl "http://localhost:8000/crime-data/incidents?lat=47.60&lon=-122.33&radius=0.05"

## Internal Structure

- client.py: [CrimeDataClient](cci:2://file:///c:/Users/tyriq.DESKTOP-U7P592K/OneDrive/Documents/Github-New/deal-scale-backend-autoscaling/backend/app/core/third_party_integrations/crime_data/client.py:7:0-34:34) composes URL from base+path, adds optional `Authorization: Bearer <key>`.
- api/proxy.py: Router (`/crime-data/health`, `/{path}`), minimal utility wrapper.
- api/routes.py: Aggregates proxy sub-router without double prefix.