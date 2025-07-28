🔧 ConflictManager Methods

1. add_conflict() – Add a new conflict with description, parties, and severity.


2. list_conflicts() – Show all conflicts (optionally filter by status).


3. resolve_conflict() – Mark a conflict as resolved and add resolution notes.


4. reopen_conflict() – Reopen a resolved conflict for further discussion.


5. delete_conflict() – Delete a conflict by its ID.


6. search_by_party() – Find conflicts involving a specific person or group.


7. filter_by_severity() – Show conflicts with a specific severity level.


8. get_statistics() – Show the number of conflicts per status (open, resolved, etc.).


9. export_conflicts_to_json() – Save all conflict data into a JSON file.


10. sort_conflicts_by_date() – Sort conflicts by creation date (newest/oldest first).


11. check_duplicate() – Check if a conflict with the same description and parties already exists.


12. get_recent_conflicts() – Show conflicts created in the last few days.


13. list_unresolved_conflicts() – List only conflicts that are still open or reopened.




---

🏷️ Conflict Class Methods

14. update_status() – Change the status of a conflict and optionally add notes.


15. __str__() – Format the conflict info for easy printing/display.
 
