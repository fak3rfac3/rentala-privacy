# Rentala Privacy Policy

This repository contains the public-facing privacy policy for the Rentala Android application, an offline-first rental-management app for independent landlords.

## Policy

- Source: [`index.html`](index.html)
- Repository page: <https://github.com/fak3rfac3/rentala-privacy/blob/main/index.html>
- Intended GitHub Pages URL: <https://fak3rfac3.github.io/rentala-privacy/>

The GitHub Pages URL is not active yet. Enable Pages in **Settings → Pages**, select **GitHub Actions** as the build and deployment source, then publish this repository. Verify the resulting URL in a signed-out browser before using it in Google Play Console.

## Updating the policy

1. Edit `index.html` and update its effective/last-updated dates when the policy changes.
2. Open a pull request against `main` and review the rendered diff.
3. Ensure the **Validate privacy policy** workflow passes before merging.
4. After Pages is enabled and deployment completes, check the live page on mobile and desktop.
5. Update the privacy-policy URL in Google Play Console if the published URL changes.

Keep the policy consistent with the app's actual release behavior. In particular, review local data handling, optional Google Drive backup, billing, permissions, and retention whenever those features change. Never commit OAuth tokens, signing keys, service-account credentials, or user backup files to this repository.

## Local validation

Requires Python 3.10 or newer; no third-party packages are needed.

```powershell
python scripts/validate_policy.py
```

## Contact

For policy questions, contact [Christian Tucay](mailto:ctucay.terre@gmail.com).
