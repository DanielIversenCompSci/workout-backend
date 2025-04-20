# workout-backend
Workout app developed for personal use as no free apps meet my needs. Create custom workoutsplits/days/sessions and log results. Will perhaps eventually develop evaluation for tracking progress.

## Database (SQL):
How the data is stored and relations explained.
E/R: https://lucid.app/lucidchart/487cb301-41b5-4ce8-9237-e68705784bc9/edit?viewport_loc=-1987%2C-1471%2C2232%2C2157%2C0_0&invitationId=inv_28121347-651e-42a8-8dca-26d4cd7c3305
#
### users table
A registered user will ged assigned a auto-incrementing unique user id and login credentiels
1. users
   id: 1 (PK)
   username: dei-user
   email: user@user.com
   password_hash: ******
   created_at: 2025-04-18
#
### workoutsessions table
When a user starts a workout, a new session is initialized and saved to the database. During this process, the user selects which workout split they are performing and which specific day within that split they are doing. For example, if they are following a Push/Pull/Legs split, they might choose to start a "Push Day" session. This relationship is tracked by saving the workout_day_id as a foreign key in the workoutsessions table. The workoutdays table in turn references the workoutsplits table, connecting each workout day back to the split it belongs to.
#
2. workoutsessions
   id: 1 (PK)
   user_: id 1 (FK)
   workout_day_id: 4 (FK)
   session_date: 2025-04-18
   notes: "my shoulder hurts today so i have lowered the weight for all exercises today"
#
### exercises table
A table will hold all exercises that can be added to the splits/days. They will be predefined from release (For now, will need to find a solution for only adding custom-added exercises locally.
#
3. exercises
  id: 3
  name: "Bicep Curl"
  description: "Grows your bicep"
  target_muscle: "Bicep"
#
