using UnityEngine;

public class LockCursor : MonoBehaviour 
{
    public bool lock;
    
    void Update() 
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            if (lock)
            {
                locked();
            }
            else
            {
                unlocked();
            }
        }
    }

    public void locked()
    {
        lock = true;
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    public void unlocked()
    {
        lock = false
        Cursor.lockState = CursorLockMode.Confined;
        Cursor.visible = true;
    }
}